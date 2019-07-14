package tower_blaster;
import java.util.*;

public class Deck {
	private  ArrayList<Integer> tower;
	
	public Deck(int initSize)
	{
		tower = new ArrayList<Integer>();
		for(int i = 1; i <= initSize; i ++) {
			tower.add(i);
		}
		
	}
	
	public void shuffle() {
		for(int i = tower.size() - 1; i >= 0; i --) {
			int rand = (int)(Math.random() * tower.size());
			int temp = tower.get(rand);
			tower.set(rand, tower.get(i));
			tower.set(i, temp);
		}
		
	}
	private boolean hasBlock(ArrayList<Integer> t, int block) {
		boolean value = false;
		for(int i = 0; i < t.size(); i++) {
			if(t.get(i).intValue() == block) {		
				return true;
			}
		}
		return value;
			
	}
	
	public int getIndex(int block){
		int index = 0;
		for(int i = 0; i < tower.size(); i ++){
			if(tower.get(i) == block){
                  index = i;
			}
		}
		return index;
	}

	public int[] newTower(int initHeight) {
		int[] newT = new int[initHeight];
		for(int i = 0; i < newT.length; i ++) {
			newT[i] = tower.remove(0);
		}
		return newT;
	}
	public String showCard(){
		   String result = Integer.toString(tower.get(0));
		   return result;
	}
	
	public void replace(int index, int[] playerT) {
		int temp = playerT[index];
		playerT[index] = tower.remove(0);
		tower.add(temp, 0);
	}

	public String displayTower(int[] pt){
		String result = "";
		for(int i = 0; i < pt.length; i ++){
            result += pt[i] + " ";
		}
		return "This is your deck: " + result;

	}
//Test
	
	public String toString() {
		String sum = "";
		for(int i = 0; i < tower.size(); i ++ ) {
			sum += Integer.toString(tower.get(i)) + "\n";
		}
		return sum;
	}
}
