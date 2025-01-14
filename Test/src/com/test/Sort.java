package com.test;

import java.util.List;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Sort {
	
	public static void main(String[] args) {
		
		List<String> list = Arrays.asList("4", "22", "310", "32", "23023", "54", "234");
		
		System.out.println(list.toString());
		
		//정렬?
		//글자수 정렬?
		//Collections.sort(list);

		//System.out.println(list.toString());
		
		//Item item = new Item();
		//System.out.println(item.toString());
		
		list.sort(new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				
				//return o2.compareTo(o1);
				return o1.length() - o2.length();
			}
			
		});
		
		System.out.println(list.toString());
		
		
	}

}

class Item {
	
	private String num = "숫자";
	
	@Override
	public String toString() {
	
		return this.num;
	}
	
}
