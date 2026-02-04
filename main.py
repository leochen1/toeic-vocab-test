from flask import Flask, render_template, jsonify, request
import PyPDF2
import os
import random
import re
from typing import List, Dict

app = Flask(__name__)

class ToeicVocabExtractor:
    def __init__(self, docs_folder='docs'):
        self.docs_folder = docs_folder
        self.vocab_data = []
        
    def extract_vocab_from_pdf(self, pdf_path):
        """從 PDF 中提取單字"""
        vocab_list = []
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                
                # 解析單字和中文翻譯
                # PDF 格式: 數字. 單字   [音標]  詞性  中文翻譯
                # 例如: 1.  abide by   [ə`baɪd]  v.  遵守、堅持（規則、法令等）
                lines = text.split('\n')
                
                for line in lines:
                    line = line.strip()
                    
                    # 跳過空行和標題行
                    if not line or 'Unit' in line or 'General Business' in line or 'Copyright' in line:
                        continue
                    
                    # 移除行首的數字編號（如 "1.  ", "2.  " 等）
                    line = re.sub(r'^\d+\.\s+', '', line)
                    
                    # 檢查是否包含音標符號 [ ]
                    if '[' in line and ']' in line:
                        # 提取單字（音標前的部分）
                        word_match = re.match(r'^([a-zA-Z][\w\s-]+?)\s+\[', line)
                        if word_match:
                            word = word_match.group(1).strip()
                            
                            # 提取音標後的內容
                            rest = line.split(']', 1)
                            if len(rest) > 1:
                                rest_text = rest[1].strip()
                                
                                # 移除詞性標記（v., n., adj., adv., prep., conj. 等，包括 n., v. 這樣的組合）
                                rest_text = re.sub(r'^(?:[a-z]+\.\s*,?\s*)+', '', rest_text)
                                
                                # 提取中文翻譯
                                translation = rest_text
                                
                                # 清理翻譯，移除括號內的補充說明
                                translation = re.sub(r'[（(].*?[)）]', '', translation).strip()
                                translation = re.sub(r'【.*?】', '', translation).strip()
                                
                                # 取第一個翻譯（用、或；分隔）
                                if '；' in translation:
                                    translation = translation.split('；')[0].strip()
                                elif '、' in translation:
                                    translation = translation.split('、')[0].strip()
                                
                                # 移除多餘空格
                                translation = ' '.join(translation.split())
                                
                                # 驗證是否包含中文
                                has_chinese = any('\u4e00' <= char <= '\u9fff' for char in translation)
                                
                                if word and translation and has_chinese and len(word.split()) <= 5:
                                    vocab_list.append({
                                        'word': word,
                                        'translation': translation,
                                        'category': os.path.basename(pdf_path).replace('.pdf', '').replace('_v1', '').replace('_v2', '')
                                    })
                
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
        
        print(f"  Loaded {len(vocab_list)} words from {os.path.basename(pdf_path)}")
        return vocab_list
    
    def load_all_vocab(self):
        """載入所有 PDF 的單字"""
        self.vocab_data = []
        pdf_files = [f for f in os.listdir(self.docs_folder) if f.endswith('.pdf')]
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.docs_folder, pdf_file)
            vocab = self.extract_vocab_from_pdf(pdf_path)
            self.vocab_data.extend(vocab)
        
        print(f"Loaded {len(self.vocab_data)} vocabulary items")
        return len(self.vocab_data)
    
    def generate_quiz(self, num_questions=10):
        """生成測驗題目"""
        if len(self.vocab_data) < num_questions * 4:
            return []
        
        # 隨機選擇題目
        selected_vocab = random.sample(self.vocab_data, num_questions)
        quiz_questions = []
        
        for vocab in selected_vocab:
            # 為每個題目生成 4 個選項
            correct_answer = vocab['translation']
            
            # 從其他單字中隨機選擇 3 個錯誤答案
            other_vocab = [v for v in self.vocab_data if v['word'] != vocab['word']]
            wrong_answers = random.sample(other_vocab, 3)
            
            options = [correct_answer] + [w['translation'] for w in wrong_answers]
            random.shuffle(options)
            
            quiz_questions.append({
                'word': vocab['word'],
                'options': options,
                'correct_answer': correct_answer,
                'category': vocab['category'],
                'example_sentence': self.generate_example_sentence(vocab['word'])
            })
        
        return quiz_questions
    
    def generate_example_sentence(self, word):
        """生成例句"""
        # 依據單字類型生成更合理的例句
        templates = {
            'contract': f"We need to review the {word} carefully before signing.",
            'agreement': f"Both parties reached an {word} on the terms.",
            'business': f"The {word} proposal was approved by the board.",
            'meeting': f"Please attend the {word} scheduled for next Monday.",
            'document': f"Make sure to keep a copy of this {word} for your records.",
            'default': [
                f"The {word} is an important part of business operations.",
                f"Understanding {word} can help improve your TOEIC score.",
                f"Many companies focus on {word} in their daily work.",
                f"Employees should be familiar with {word}.",
                f"The concept of {word} is widely used in business English."
            ]
        }
        
        # 檢查單字類型
        word_lower = word.lower()
        for key in templates:
            if key in word_lower:
                if key == 'default':
                    return random.choice(templates[key])
                return templates[key]
        
        # 使用預設模板
        return random.choice(templates['default'])

# 初始化提取器
extractor = ToeicVocabExtractor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/load-vocab', methods=['GET'])
def load_vocab():
    """載入單字資料"""
    count = extractor.load_all_vocab()
    return jsonify({'status': 'success', 'count': count})

@app.route('/api/generate-quiz', methods=['GET'])
def generate_quiz():
    """生成測驗"""
    quiz = extractor.generate_quiz(10)
    # 不發送正確答案到前端
    quiz_for_client = []
    for q in quiz:
        quiz_for_client.append({
            'word': q['word'],
            'options': q['options'],
            'category': q['category']
        })
    return jsonify({'questions': quiz_for_client})

@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    """提交測驗並評分"""
    data = request.json
    user_answers = data.get('answers', [])
    
    # 重新生成相同的測驗（使用相同的隨機種子或保存在 session 中）
    # 這裡簡化處理，從請求中接收單字列表
    words = data.get('words', [])
    
    results = []
    score = 0
    
    # 找到對應的單字並檢查答案
    for i, word in enumerate(words):
        vocab_item = next((v for v in extractor.vocab_data if v['word'] == word), None)
        if vocab_item:
            correct_answer = vocab_item['translation']
            user_answer = user_answers[i] if i < len(user_answers) else ''
            is_correct = user_answer == correct_answer
            
            if is_correct:
                score += 1
            
            results.append({
                'word': word,
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': is_correct,
                'explanation': f"{word} 的意思是「{correct_answer}」",
                'example_sentence': extractor.generate_example_sentence(word)
            })
    
    return jsonify({
        'score': score,
        'total': len(words),
        'results': results
    })

if __name__ == '__main__':
    # 啟動時載入單字
    print("Loading vocabulary from PDFs...")
    extractor.load_all_vocab()
    
    # 雲端部署時使用環境變數設定 port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
