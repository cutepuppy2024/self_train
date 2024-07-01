students = [
    [1, '홍길동', 100, 100, 99, 299, 96.67,1],
    [2, '유관순', 99, 99, 98, 296, 98.67,1], 
    [3, '강감찬', 80, 80, 81, 241, 80.33,1],
    [4, '김구', 100, 100, 90, 290, 96.67,1],
    [5, '김유신', 90, 70, 50, 210, 70.0,1],
    [6, '이순신', 100, 100, 100, 300, 300.0,1]
]
search_txt =['',
            '찾고자 하는 학생의 이름을 검색하세요 >>',
            '총점 이상',
            '총점 이하']
s_sort = ['','국어','영어','수학']

cnt = len(students)+1
while True:
    print('-'*40)
    print(' [ 학생성적프로그램  ]')
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >>')
    if not choice.isdigit():
        print('숫자만 가능합니다')
        continue
    choice = int(choice)

    if choice == 1:
        print('학생성적 입력')
        name = input('학생의 이름을 입력하세요 (0.취소)>>')
        if name == '0': break
        kor = int(input('국어성적 >>'))
        eng = int(input('영어성적 >>'))
        math = int(input('수학성적 >>'))
        total = kor + eng + math
        avg = float(f'{total/3:.2f}')
        rank = 1
        stuNo = cnt
        stu = [stuNo, name, kor, eng, math, total, avg, rank]
        students.append(stu)
        cnt += 1

    elif choice == 2:
        print(' [ 학생성적 전체출력 ]')
        print('-'*40)
        print('번호\t이름\t국어\t영어\t수학\t합계\t총점\t등수')
        print('-'*40)
        for stu in students:
            for i in stu:
                print(i,end='\t')
            print()

    elif choice == 3:
        while True:
            print('학생검색')
            print('-'*40)
            print('1. 학생이름으로 검색')
            print('2. 총점 이상')
            print('3. 총점 이하')
            choice = int(input('원하는 번호를 입력하세요(0.취소) >>'))
            if choice == 0: break
            elif choice == 1:
                search = input(search_txt[choice])
            else:
                search = int(input(search_txt[choice]))

            s_list=[]
            for stu in students:
                if choice == 1:
                    if stu[1].find(search) != -1:
                        s_list.append(stu)
                elif choice == 2:
                    if stu[5] >= search:
                        s_list.append(stu)
                elif choice == 3:
                    if stu[5] <= search:
                        s_list.append(stu)

            if len(s_list) != 0:
                print('-'*40)
                print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
                print('-'*40)
                for i in s_list:
                    for j in i:
                        print(j,end='\t')
                    print()
            else :
                print('찾고자 하는 사람이 명단에 없습니다. 다시 입력해 주세요')
                break
                
    elif choice == 4:
        print('학생성적 수정')
        search = input('찾고자 하는 학생의 이름을 입력하세요(0.취소) >>')
        if search == '0': break
        cnt = 0
        for stu in students:
            if stu[1] == search:
                break
            cnt += 1

        if cnt == len(students):
            print('찾고자 하는 학생이 존재하지 않습니다.') 
        else:    
            print(f'{search} 학생이 존재합니다.')
            print(' 수정할 과목 ')
            print('1. 국어')
            print('2. 영어')
            print('3. 수학')
            choice = int(input('원하는 과목을 선택하세요 >>'))

            if choice == 1:
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][choice+1]} ')
                students[cnt][choice+1] = int(input(f'변경할 {s_sort[choice]}점수 입력 >>'))
                students[cnt][5] = students[cnt][2] + students[cnt][3] + students[cnt][4]
                students[cnt][6] = float(f'{students[cnt][5]/3:.2f}')
                print(students[cnt])
                
            elif choice ==2:
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][choice+1]} ')
                students[cnt][choice+1] = int(input(f'변경할 {s_sort[choice]}점수 입력 >>'))
                students[cnt][5] = students[cnt][2] + students[cnt][3] + students[cnt][4]
                students[cnt][6] = float(f'{students[cnt][5]/3:.2f}')
                print(students[cnt])
            
            elif choice ==3:
                print(f'{search} 학생의 현재 {s_sort[choice]} 성적은 {students[cnt][choice+1]} ')
                students[cnt][choice+1] = int(input(f'변경할 {s_sort[choice]}점수 입력 >>'))
                students[cnt][5] = students[cnt][2] + students[cnt][3] + students[cnt][4]
                students[cnt][6] = float(f'{students[cnt][5]/3:.2f}')
                print(students[cnt])

    elif choice == 5:
        print('등수처리')
        choice == int(input('등수처리 하시겠습니까? (0.취소)'))
        if choice == 0: break
        for i in students:
            rank_cnt = 1
            for j in students:
                if i[5] < j[5]:
                    rank_cnt += 1
                i[7] = rank_cnt
        print(students)

    elif choice == 6:
        print('학생 삭제')
        search = input('찾고자 하는 학생의 이름을 검색하세요(0.취소) >> ')
        cnt = 0
        for stu in students:
            if stu[1] == search :
                break
            cnt += 1
        
        if cnt == len(students):
            print(f'{search} 학생이 명단에 존재하지 않습니다. 다시 입력하세요')
        else:
            print(f'{search} 학생이 명단에 존재합니다.')
            choice = int(input('원하는 작업을 선택하세요 (1. 삭제, 0. 취소)'))
            if choice == 0 : break
            elif choice == 1:
                del students[cnt]
                print(f'{search} 학생이 명단에서 삭제되었습니다.')
            else : 
                print('잘못 누르셨습니다. 다시 입력하세요')

    elif choice == 0:
        print('프로그램 종료')
        break