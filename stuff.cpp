#include <iostream>
#include <string>
using namespace std;

string num(int starting){
	int length=(to_string(starting)).length();
	string place[]={" "," "," hundred "," thousand "," "," hundred "," million "," "," hundred "," billion "};
	string ones[]={"","one","two","three","four","five","six","seven","eight","nine"};
	string tens[]={"","onety","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"};
	string wrd="";
	int arr[length];
	for(int i=length-1;i>=0;i--){//Turning the number into an array
    		arr[i] = starting % 10;
    		starting /= 10;
	}
	for(int i=length-1;i>=0;i--){//replacing the # with a word
		if(length-i-1==1||length-i-1==4||length-i-1==7){//This decideds if it should be in the ones or the tens
			if(tens[arr[i]]=="onety"){
			    if(arr[i+1]==0){
			        wrd="test 0"+place[length-i-1]+wrd;
			    }else if(arr[i+1]==1){
			        wrd="test 1"+place[length-i-1]+wrd;
			    }else if(arr[i+1]==2){
			        wrd="test 2"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==3){
			        wrd="test 3"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==4){
	                wrd="test 4"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==5){
	                wrd="test 5"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==6){
	                wrd="test 6"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==7){
	                wrd="test 7"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==8){
	                wrd="test 8"+place[length-i-1]+wrd;
	            }else if(arr[i+1]==9){
	                wrd="test 9"+place[length-i-1]+wrd;
	            }
			}else{
			    wrd=tens[arr[i]]+place[length-i-1]+wrd;
			}
		}else{
			wrd=ones[arr[i]]+place[length-i-1]+wrd;
		}
	}
	return wrd;
}

int main(){
	int starting=696969;
	cout<<"Enter your number.\n";
	cin>>starting;
	cout<<num(starting);
	return 0;
}
