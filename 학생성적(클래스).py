# with open("stu.txt","w",encoding='utf8') as f:
#     while True:
#         s_i = input('내용을 입력(0.취소) >>')
#         if s_i == '0': break
#         f.write(s_i+"\n")
#     print()


# 1,홍길동,100,100,99,299,96.67,1
# 2,유관순,99,99,98,296,98.67,1 
# 3,강감찬,80,80,81,241,80.33,1
# 4,김구,100,100,90,290,96.67,1
# 5,김유신,90,70,50,210,70.0,1

         

#-----------------------------------------------------
# Student 클래스
#-----------------------------------------------------

class Student:
    count = 1

    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float(f"{self.total/3:.2f}")
        self.rank = rank
    
    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"
    

#-----------------------------------------------------
# 파일 불러와서 저장하기
#-----------------------------------------------------
    
students = []
f = open("stu.txt","r",encoding='utf8')
while True:
    txt = f.readline()
    if txt == '': break
    txt_list = txt.split(',')
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()


# 파일 불러오기 한 후 학생수에서 +1 추가
Student.count = len(students)+1

#-----------------------------------------------------
# 함수부분
#-----------------------------------------------------
search_txt=['',
            '찾고자 하는 학생의 이름을 검색하세요 >>',
            '총점 이상 >>',
            '총점 이하 >>']


while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력 ')
    print('2. 학생성적전체출력')
    print('3. 학생성적 검색')
    print('4. 학생성적 수정')
    print('5. 학생성적 삭제')
    print('6. 등수처리')
    print('0. 종료')
    print('-'*40)
    choice = input("원하는 번호를 입력하세요 >>")
    choice = int(choice)

    if choice == 1:
        name = input(f'{len(students)+1}학생의 이름을 입력하세요 (0.취소)>>')
        if name == '0': break
        kor = int(input('국어 성적을 입력하세요 >>'))
        eng = int(input('영어 성적을 입력하세요 >>'))
        math = int(input('수학 성적을 입력하세요 >>'))

        s = Student(name,kor,eng, math)
        students.append(s)
        print("입력 데이터 :",s)

    elif choice == 2:
        print('[학생성적출력]')
        print('-'*60)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print('-'*60)
        for s in students:
            print(s)
        print()
        
    elif choice == 3:
        while True:
            print('[학생성적 검색]')
            print('-'*40)
            print('1. 학생이름으로 검색')
            print('2. 총점이상 검색')
            print('3. 총점이하 검색')
            print('0. 이전화면 이동')
            choice = int(input('원하는 번호를 입력하세요(0.취소) >>'))
            if choice == '0': break
            if choice == 1:
                search = input(search_txt[choice])
            else :
                search = int(input(search_txt[choice]))

            s_list = []
            for i in students:
                if choice == 1:
                    if i.name.find(search) != -1:
                        s_list.append(i)                       
                elif choice == 2:
                    if i.total >= search:
                        s_list.append(i)
                elif choice == 3:
                    if i.total <= search:
                        s_list.append(i)
            if len(s_list) != 0 :
                print('[학생성적 출력]')
                print('-'*60)
                print('번호\t이름\t국어\t영어\t수학\t합계\t총점\t등수')
                print('-'*60)
                for i in s_list:
                    print(i)
            else:
                print("찾고자 하는 학생이 없습니다. 다시 검색하세요")

    elif choice == 4:
        search = input('찾고자 하는 이름을 입력하세요 >>')

        cnt = 0
        for s in students:
            if s.name == search:
                break
        cnt += 1

        if cnt == len(students):
            print("찾고자 하는 학생이 없습니다. 다시 검색하세요")

        else:
            print(f'{search}으로 검색한 학생을 찾았습니다.')
            print()
            print(' [수정할 과목 선택]')
            print('-'*40)
            print('1. 국어 ')
            print('2. 영어 ')
            print('3. 수학 ')
            print('-'*40)
            choice = int(input('원하는 번호를 입력하세요 >>'))

            if choice == 1:
                print(f'변경전 점수 : {students[cnt].kor}')
                students[cnt].kor = int(input('변경할 점수를 입력하세요 >>'))
                students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                students[cnt].avg = float(f'{students[cnt].total/3:.2f}')
                print(f'{students[cnt].kor}로 점수가 변경되었습니다.')
                print(students[cnt])

            elif choice == 2:
                print(f'변경전 점수 : {students[cnt].eng}')
                students[cnt].eng = int(input('변경할 점수를 입력하세요 >>'))
                students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                students[cnt].avg = float(f'{students[cnt].total/3:.2f}')
                print(students[cnt])

            elif choice == 3:
                print(f'변경전 점수 : {students[cnt].math}')
                students[cnt].math = int(input('변경할 점수를 입력하세요 >>'))
                students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                students[cnt].avg = float(f'{students[cnt].total/3:.2f}')
                print(students[cnt])


    elif choice == 5:
        search = input('삭제하고자 하는 이름을 입력하세요 >>')
        cnt = 0
        for s in students :
            if s.name == search :
                break
            cnt += 1
        if cnt >= len(students):
            print('찾고자 하는 학생이 없습니다. 다시 겁색하세요')

        else :
            print(f'{search}으로 검색한 학생을 찾았습니다.')
            print()
            print(' [ 학생성적 삭제 ]')
            print('-'*40)
            choice = int(input('원하는 번호를 입력하세요 >>'))

            if choice == 1:
                del students[cnt]
                print(f'{search} 학생 성적이 삭제 되었습니다.')

            else :
                print('학생성적 삭제를 취소하셨습니다.')
            
    elif choice == 6:
        print('등수처리를 진행하시겠습니까? >>')
        print('1.진행')
        print('0.취소')
        choice = int(input('원하는 번호를 입력하세요 >>'))

        if choice == 1 :
            for i in students:
                rank_cnt = 1
                for j in students:
                    if i.total < j.total:
                        rank_cnt += 1
                    i.rank = rank_cnt
        print('등수처리가 완료되었습니다.')

    elif choice == 0:
        print('프로그램을 종료합니다.')
        break

