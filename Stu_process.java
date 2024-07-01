package h_java;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

public class Stu_process {
	Scanner scan = new Scanner(System.in);
	
	String[] title = {"학번","이름","국어","영어","수학","합계","평균","등수"};
	String stuNo;
	String name;
	int kor, eng, math, total, rank;
	double avg;
	int choice = 0;
	
	// 화면부분
	int main_screen(ArrayList list) {
		System.out.println(" [ 학생성적 프로그램 ] ");
		System.out.printf("1. 성적입력 (현재 입력되어 있는 학생 수 : %d명) \n",list.size());
		System.out.println("2. 성적출력");
		System.out.println("3. 성적수정");
		System.out.println("4. 학생검색");
		System.out.println("5. 학생삭제");
		System.out.println("6. 등수처리");
		System.out.println("0. 프로그램 종료");
		System.out.println("-----------------------------------");
		System.out.println("원하는 번호를 입력하세요");
		choice = scan.nextInt();
		scan.nextLine();
		return choice;
	}
	
	// 성적입력 메서드
	void stu_input(ArrayList list) {
		while(true) {
			System.out.println(" [ 성적입력 ] ");
	
			// 이름입력
			System.out.printf("%d번째 학생의 이름을 입력하세요(0.취소) >> \n",list.size()+1);
			name = scan.nextLine();
			if(name.equals("0")) {
				System.out.println("이전화면으로 돌아갑니다.");
				break;
			}
			
			
			// 국영수입력
			System.out.println("국어성적을 입력하세요 >>");
			kor = scan.nextInt();
			System.out.println("영어성적을 입력하세요 >>");
			eng = scan.nextInt();
			System.out.println("수학성적을 입력하세요 >>");
			math = scan.nextInt();
			scan.nextLine();
			
			list.add(new Stu_score(name,kor,eng,math));
			
			System.out.printf("%s 학생의 성적입력이 완료되었습니다. \n",name);
			System.out.println();
			
			}// while
	}// stu_input
	
	// 성적출력 메서드
	void stu_print(ArrayList list) {
		System.out.println(" [ 성적출력 ] ");
		// title
		for(int i=0;i<title.length;i++) {
			System.out.printf("%s\t",title[i]);
		}
		System.out.println();
		System.out.println("--------------------------------");
		
		if(list.size()==0) {
			System.out.println("출력할 성적이 없습니다");
			System.out.println();
			return;
		}
		
		// data
		for(int i=0;i<list.size();i++) {
			Stu_score s = (Stu_score)list.get(i);
			System.out.printf("%s\t%s\t%d\t%d\t%d\t%d\t%.2f\t%d\t",
					s.stuNo,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank);
			System.out.println();
		}//for
	}// stu_print
	
	void score_correct(ArrayList list) {
			// 학생검색 메서드
			int temp_no = stu_search(list);
			
			if (temp_no == -1) {
				System.out.println("찾고자 하는 학생이 존재하지 않습니다. 다시 입력하세요");
			}
			
			Stu_score s = (Stu_score) list.get(temp_no);
			
			// 과목선택 -> 수정

			System.out.println(" 수정할 과목 선택 (0.취소) >>");
			System.out.println("1. 국어성적");
			System.out.println("2. 영어성적");
			System.out.println("3. 수학성적");
			System.out.println("-----------------------");
			System.out.println("원하는 번호를 입력하세요 ");
			choice = scan.nextInt();
			scan.nextLine();

			switch(choice) {
			case 1 : sub_choice(s,s.kor,choice); break;
			case 2 : sub_choice(s,s.eng,choice); break;
			case 3 : sub_choice(s,s.math,choice); break;
			}// switch
			
	}// score_correct
	
	// 학생성적검색 메서드
	void score_search(ArrayList list) {
		System.out.println(" [ 성적검색 ] ");
		System.out.println("1. 이름검색");
		System.out.println("2. 합계검색");
		System.out.println("3. 평균검색");
		System.out.println("--------------------");
		System.out.println("원하는 번호를 입력하세요");
		choice = scan.nextInt();
		scan.nextLine();
		
		ArrayList searchList = new ArrayList();
		String s_name ="";
		int s_total = 0;
		double s_avg = 0;
		
		switch(choice) {
		case 1: //이름
			System.out.println("찾고자 하는 학생의 이름을 입력하세요 >>");
			s_name = scan.nextLine();
			
			for(int i=0;i<list.size();i++) {
				Stu_score s = (Stu_score)list.get(i);
				if(s.name.contains(s_name)) {
					searchList.add(s);
				}
			}// for
			stu_print(searchList);
			System.out.println();
			break;
			
		case 2: // 합계
			System.out.println("합계 성적을 입력하세요 >>");
			s_total = scan.nextInt();
			
			for(int i=0;i<list.size();i++) {
				Stu_score s = (Stu_score)list.get(i);
				if(s.total>= s_total) {
					searchList.add(s);
				}
			}// for
			stu_print(searchList);
			System.out.println();
			break;
			
		case 3: // 평균
			System.out.println("평균 성적을 입력하세요 >>");
			s_avg = scan.nextInt();
			
			for(int i=0;i<list.size();i++) {
				Stu_score s = (Stu_score)list.get(i);
				if(s.avg>= s_avg) {
					searchList.add(s);
				}
			}// for
			stu_print(searchList);
			System.out.println();
			break;
			}// switch
		}// score_search

	// 학생삭제 메서드
	void stu_delete(ArrayList list) {
		System.out.println(" [ 학생삭제 ] ");
		
		int temp_no = stu_search(list);
		
		if(temp_no==-1) {
			System.out.println("검색한 학생의 이름이 존재하지 않습니다. 다시 입력하세요 >>");
			System.out.println();
			return;
		}
		
		Stu_score s = (Stu_score) list.get(temp_no);
		System.out.printf("%s 학생을 정말 삭제하시겠습니까? (1.삭제, 0.취소) >>",s.name);
		int choice = scan.nextInt();
		
		if(choice==1) {
			list.remove(temp_no);
			System.out.println("삭제가 완료되었습니다.");
			System.out.println();
		}else {
			System.out.println("삭제를 취소합니다.");
			System.out.println();
		}

	}// stu_delete
	
	// 등수처리 메서드
	void stu_rank(ArrayList list) {
		System.out.println(" [ 등수처리 ] ");
		for(int i=0;i<list.size();i++) {
			int c_rank = 1;
			for(int j=0;j<list.size();j++) {
				Stu_score s1 = (Stu_score)list.get(i);
				Stu_score s2 = (Stu_score)list.get(j);
				if(s1.total<s2.total) {
					c_rank++;
				}
				s1.rank = c_rank;
			}
		}//for
		System.out.println("등수처리가 완료되었습니다.");
		System.out.println();
	}// stu_rank
	

//-------------------------------------------------------------------------
	// sub_method
	// 학생검색 메서드	
	int stu_search(ArrayList list) {
		System.out.println(" [ 학생검색 ] ");
		System.out.println("찾고자 하는 학생의 이름을 검색하세요 (0.취소) >>");
		
		String search = scan.nextLine();

		int temp_no = -1;
		for(int i=0;i<list.size();i++) {
			Stu_score s = (Stu_score)list.get(i);
			if(s.name.equals(search)) {
				System.out.printf("%s 학생을 찾았습니다.",search);
				temp_no = i;; // 학생의 위치
				break;
			}
		}// for
		return temp_no;
	}// stu_search
	
	// 과목선택 메서드
	void sub_choice(Stu_score s, int score, int choice) {
		System.out.printf("현재 %s 성적은 %d 입니다.",title[choice+1],score);
		System.out.println("변경할 성적을 입력하세요");
		score = scan.nextInt();
		
		if (choice==1) s.kor = score;
		else if (choice == 2) s.eng = score;
		else s.math = score;
		
		s.total = kor + eng + math;
		s.avg = total/3.0;
		System.out.printf("변경된 %s 성적은 %d 입니다.",title[choice+1],score);
		System.out.printf("%s 성적변경이 완료되었습니다.", title[choice+1]);
		System.out.println();
	}// sub_choice

	
	
}// class
