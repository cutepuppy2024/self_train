package h_java;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.ArrayList;

public class Stu_score {
	
	static int count = 1; 
	{// 초기화 블럭
		// 학번 자동생성
		Date d = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yy");
		stuNo = "S"+sdf.format(d) + String.format("%03d",count++);
		
	}
	
	Stu_score(){}// 기본생성자
	Stu_score(String name, int kor, int eng, int math){
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		this.total = kor+eng+math;
		this.avg = total/3.0;
	}
	
	String getStuNo() {
		return stuNo;
	}
	
	void setStuNo(String stuNo) {
		this.stuNo = stuNo;
	}
	
	String[] title = {"학번","이름","국어","영어","수학","합계","평균","등수"};
	String stuNo;
	String name;
	int kor, eng, math, total, rank;
	double avg;
	int choice = 0;
}
