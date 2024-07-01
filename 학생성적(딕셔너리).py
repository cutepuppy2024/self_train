import stu_file

students = stu_file.stu_open()
txt_list = ['',
            "찾고자 하는 학생의 이름을 입력하세요 >>",
            "총점 이상 검색",
            "총점 이하 검색"]
s_sort = ['', '국어', '영어', '수학']

cnt = len(students)+1
while True:
    print(' [ 학생 성적처리 프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7. 학생성적 파일 저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >>')
    if not choice.isdigit():
        print('숫자가 아닙니다. 다시 입력하세요')
        continue
    choice = int(choice)

    if choice == 1:
        print(' [ 학생성적 입력 ]')
        name = input('학생이름을 입력하세요 (0. 취소) >>')
        if name == '0' : break

        student = {}
        
        student["stuNo"] = cnt
        student["name"] = name
        kor = int(input('국어성적 입력 >>'))
        student["kor"] = kor
        eng = int(input("영어성적 입력 >>"))
        student["eng"] = eng
        math = int(input("수학성적 입력 >>"))
        student["math"] = math
        total = kor + eng + math
        student["total"] = total
        avg = float(f'{total/3:.2f}')
        student["avg"] = avg 
        rank = 1
        student["rank"] = rank 

        students.append(student) 
        cnt += 1    
        print(student)

    elif choice == 2:
        print('-'*40)
        print(' [ 학생성적 전체출력 ] ')
        print('-'*65)
        print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print('-'*65)
        for s_dic in students:
            for key in s_dic:
                print(s_dic[key],end='\t')
            print()
        print('-'*65)
        print()


    elif choice == 3:
        while True:
            print(' [ 학생성적 검색 ]')
            print('-'*50)
            print('1. 학생이름으로 선택')
            print('2. 총점 이상')
            print('3. 총점 이하')
            print('-'*50)
            choice = int(input('원하는 번호를 선택하세요 >>'))

            if choice == 1:
                search = input(txt_list[choice])
            else:
                search = int(input(txt_list[choice]))

            s_list = []
            for i in students:
                if choice == 1:
                    if i['name'].find(search) != -1:
                        s_list.append(i)
                elif choice == 2:
                    if int(s_dic['total']) >= search:
                        s_list.append(s_dic)
                elif choice == 3:
                    if s_dic['total'] <= search:
                        s_list.append(s_dic)

            if len(s_list) != 0:
                print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
                print('-'*50)
                for i in s_list:
                    for key in i:
                        print(i[key],end='\t')
                    print()
            else:
                print('찾고자 하는 학생이 존재하지 않습니다')

    elif choice == 4:
        print(' [ 학생성적 수정 ]')
        search = input('찾고자 하는 학생의 이름을 입력하세요 >>')
        cnt = 0
        for s_dic in students:
            if s_dic["name"] == search:                
                break
            cnt += 1
        
        if len(students) == cnt:
            print('찾고자 하는 학생의 이름이 명단에 존재하지 않습니다. 다시 입력해 주세요')
 
        else: 
            print(f'{search} 학생이 명단에 존재합니다.')
            print(' [ 수정 과목 선택 ]')
            print('1. 국어')
            print('2. 영어')
            print('3. 수학')
            choice = int(input('수정할 과목을 선택하세요 >>'))

            if choice == 1:
                s_1 = 'kor'
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][s_1]} 입니다.')
                students[cnt][s_1] = int(input('변경할 성적을 입력하세요 >>'))
                students[cnt]["total"] = students[cnt]['kor'] + students[cnt]['eng'] + students[cnt]['math']
                students[cnt]['avg'] = float(f'{students[cnt]['total']/3:.2f}')
                print(f'{search} 학생의 {s_sort[choice]}성적이 {students[cnt][s_1]}으로 변경되었습니다.') 
                print(students[cnt])   
            elif choice == 2:
                s_1 = 'eng'
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][s_1]} 입니다.')
                students[cnt][s_1] = int(input('변경할 성적을 입력하세요 >>'))
                students[cnt]["total"] = students[cnt]['kor'] + students[cnt]['eng'] + students[cnt]['math']
                students[cnt]['avg'] = float(f'{students[cnt]['total']/3:.2f}')
                print(f'{search} 학생의 {s_sort[choice]}성적이 {students[cnt][s_1]}으로 변경되었습니다.') 
                print(students[cnt])   
            elif choice == 3:
                s_1 = 'math'
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][s_1]} 입니다.')
                students[cnt][s_1] = int(input('변경할 성적을 입력하세요 >>'))
                students[cnt]["total"] = students[cnt]['kor'] + students[cnt]['eng'] + students[cnt]['math']
                students[cnt]['avg'] = float(f'{students[cnt]['total']/3:.2f}')
                print(f'{search} 학생의 {s_sort[choice]}성적이 {students[cnt][s_1]}으로 변경되었습니다.') 
                print(students[cnt])   


    elif choice == 5:
        print(' [ 등수처리 ]')
        choice = int(input('등수처리 하시겠습니까?(0. 취소) >>'))
        if choice == '0': break

        for s_dic in students:
            rank_cnt = 1
            for c_dic in students:
                if s_dic['total'] < c_dic['total']:
                    rank_cnt += 1
                s_dic['rank'] = rank_cnt

        print('등수처리가 완료되었습니다')        
        print(students)
        print()

    elif choice == 6:
        print(' [ 학생 성적 삭제 ]')
        search = input('찾고자 하는 학생의 이름을 입력하세요 >>')
        cnt = 0
        for s_dic in students:
            if s_dic['name'] == search:
                break
            cnt += 1
        if cnt == len(students):
            print('찾고자 하는 학생의 이름이 명단에 존재하지 않습니다.')

        else:
            print(f'{search} 학생이 명단에 존재합니다.')
            choice = int(input('삭제하시겠습니까? (1. 삭제,  0.취소)'))
            if choice == 0:  break
            elif choice == 1:
                del students[cnt]
            else:
                print('잘못 입력하셨습니다')

    elif choice == 7:
        with open("stu.txt","w",encoding='utf8') as f:
            for s_dic in students:
                stuNo = s_dic["stuNo"]
                name = s_dic["name"]
                kor = s_dic["kor"]
                eng = s_dic["eng"]
                math = s_dic["math"]
                total = s_dic["total"]
                avg = s_dic["avg"]
                rank = s_dic["rank"]

                f.write(f'{stuNo},{name},{kor},{eng},{math},{total},{avg},{rank}')
            print('모든 내용이 파일에 저장되었습니다')
            print()


    elif choice == 0:
        print('프로그램 종료')


# 1,홍길동,100,100,99,299,96.67,1
# 2,유관순,99,99,98,296,98.67,1 
# 3,강감찬,80,80,81,241,80.33,1
# 4,김구,100,100,90,290,96.67,1
# 5,김유신,90,70,50,210,70.0,1