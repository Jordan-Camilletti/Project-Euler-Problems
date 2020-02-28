/*A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.*/
package main;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main{
	public static String getLongest(Map<String, ArrayList<String>> m){//Returns the map value with the longest array list
		int longest=0;
		String rtn="";
		for(Map.Entry<String, ArrayList<String>> entry:m.entrySet()){
			if(entry.getValue().size()>=longest){
				longest=entry.getValue().size();
				rtn=entry.getKey();
			}
		}
		return(rtn);
	}
	
	public static void main(String[] args){
		ArrayList<String> values=new ArrayList<String>();//Original 3 length codes
		String password="";
		String longest;
		Map<String, ArrayList<String>> nums=new HashMap<String, ArrayList<String>>();
		try{
			File f=new File("keylog");//Reading file
			BufferedReader br=new BufferedReader(new FileReader(f));
			String line;
			while((line=br.readLine())!=null){
				if(!values.contains(line)){//Doesn't add duplicates
					values.add(line);
					String[] vals=line.split("");//Used to get each individual number in the code
					for(int n=0;n<3;n++){
						if(nums.get(vals[n])==null){
							nums.put(vals[n], new ArrayList<String>());
						}
					}
					for(int n=1;n<=3;n++){//This is just a fancy way of counting 00->01->02->12
						if(!nums.get(vals[n/3]).contains(vals[1+(n/2)]))
							nums.get(vals[n/3]).add(vals[1+(n/2)]);
					}
				}
			}
		}catch(FileNotFoundException e){
			System.out.println(e);
		}catch(IOException e){
			System.out.println(e);
		}
		//System.out.println(values);
		//System.out.println(nums);//Numbers found along with an array of what numbers come after it
		while(nums.size()>0){//Loops through until all digits have been added
			longest=getLongest(nums);//Gets number in front of the most digits and adds it to the front
			//System.out.println(longest);
			password+=longest;
			nums.remove(longest);//Removes said number from map
		}		
		System.out.println(password);
	}
}
