package h_java;

import java.util.ArrayList;
import java.util.Scanner;

public class Stu_Main {

	public static void main(String[] args) {
		// 학생성적프로그램 구현
		Scanner scan = new Scanner(System.in);
		
		Stu_process sp = new Stu_process();
		ArrayList list = new ArrayList();
		list.add(new Stu_score("홍길동",100,100,100)); // 확인용
		
		while(true) {
			// 화면부분
			int choice = sp.main_screen(list);
			
			switch(choice) {
			case 1:
				sp.stu_input(list);
				break;
				
			case 2:
				sp.stu_print(list);
				break;
				
			case 3:
				sp.score_correct(list);
				break;
				
			case 4:
				sp.score_search(list);
				break;
				
			case 5:
				sp.stu_delete(list);
				break;
				
			case 6: 
				sp.stu_rank(list);
				break;
				
			case 0:
				System.out.println("프로그램을 종료합니다");
				break;
			}// switch
			
		}//while

	}// main

}// class
