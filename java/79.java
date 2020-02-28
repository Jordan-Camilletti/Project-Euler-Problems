/*A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.*/
package main;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main{
	public static void main(String[] args){
		ArrayList<String> values=new ArrayList<String>();//Original 3 length codes
		String password="";
		Map<String, ArrayList<String>> nums=new HashMap<String, ArrayList<String>>();//maps numbers to list of numbers after it
		try{
			File f=new File("keylog");//Reading file
			BufferedReader br=new BufferedReader(new FileReader(f));
			String line;
			while((line=br.readLine())!=null){
				if(!values.contains(line)){//Doesn't add duplicates
					values.add(line);
					String[] vals=line.split("");//Used to get each individual number in the code
					if(nums.get(vals[0])==null){
						nums.put(vals[0], new ArrayList<String>());
					}
					if(nums.get(vals[1])==null){
						nums.put(vals[1], new ArrayList<String>());
					}
					if(!nums.get(vals[0]).contains(vals[1]))//Doesn't add duplicates
						nums.get(vals[0]).add(vals[1]);
					if(!nums.get(vals[0]).contains(vals[2]))
						nums.get(vals[0]).add(vals[2]);
					if(!nums.get(vals[1]).contains(vals[2]))
						nums.get(vals[1]).add(vals[2]);
				}
			}
		}catch(FileNotFoundException e){
			System.out.println(e);
		}catch(IOException e){
			System.out.println(e);
		}
		System.out.println(values);
		System.out.println(nums);//Numbers found along with an array of what numbers come after it
	}
}
