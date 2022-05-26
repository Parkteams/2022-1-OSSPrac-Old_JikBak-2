from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name') # 받은 값들을 넣어줌 major 까지
      result["StudentNumber"] = request.form.get("StudentNumber")
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')
      Pl=[]#리스트 생성
      if request.form.get('PL1')!=None: # 받아온 checkbox 값이 none 이면 넣지않고 아니면 넣음 
         Pl.append(request.form.get('PL1'))
      if request.form.get('PL2')!=None:
         Pl.append(request.form.get('PL2'))
      if request.form.get('PL3')!=None:
         Pl.append(request.form.get('PL3'))
      if request.form.get('PL4')!=None:
         Pl.append(request.form.get('PL4'))
      
      result['Programming Languages'] =','.join(Pl) #리스트를 '를 기준으로 분해후 넣어줌 
      
      # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port=80) # nginX 의 포트가 80이라서 때문에 
   #이를 설정하지 않으면 컨테이너화해도 nginX와 포트를 공유하지 못해 웹 페이지가 정상적으로 열지 못한다.
