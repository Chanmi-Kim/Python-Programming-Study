package com.test;

import java.util.ArrayList;

public class Test {
	
	public static void main(String[] args) {
		
		ArrayList<String> words = new ArrayList<String>();
		
		words.add("hot");
		words.add("dot");
		words.add("dog");
		words.add("lot");
		words.add("log");
		words.add("log");
		
		String begin = "hit";
		String target = "cog";
		
		int count = 0;
		int size = words.size();
		
		for (int i=0; i<size; i++) {
			
			if (isSimilar(begin, words.get(i))) {
				
			}
		}
		
		
	}
	
	public static boolean isSimilar(String a, String b) {
		
		for (int i=0; i<a.length(); i++) {
			for (int j=0; j<b.length(); j++) {
				if (a.replace(a.substring(i, i+1), "").equals(b.replace(b.substring(j, j+1), ""))) {
					return true;
				}
			}
		}
		
		return false;
		
	}

}







