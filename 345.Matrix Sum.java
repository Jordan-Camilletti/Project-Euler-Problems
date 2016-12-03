/**/

package main;

public class Main{
 	public static void main(String []args){
    		String r1[]="7 53 183 439 863".split(" ");
             	String r2[]="497 383 563 79 973".split(" ");
                        String r3[]="287 63 343 169 583".split(" ");
                        String r4[]="627 343 773 959 943".split(" ");
                        String r5[]="767 473 103 699 303".split(" ");
                         int top1,top2,top3,top4,top5;
                         for(int x=0;x<5;x++){
                            	if(r1[x]>top1){
                            		top1=r1[x];
                            	}
                            	if(r2[x]>top2){
                            		top2=r2[x];
                            	}
                            	if(r3[x]>top3){
                            		top3=r3[x];
                            	}
                            	if(r3[x]>top3){
                            		top3=r3[x];
                            	}
                            	if(r3[x]>top3){
                            		top3=r3[x];
                            	}	
                         }
		System.out.print(top1+top2+top3+top4+top5);
 	}
}
