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

	public Deck(ArrayList<Integer> t){
		tower = t;
	}
	
	public void shuffle() {
		for(int i = tower.size() - 1; i >= 0; i --) {
			int rand = (int)(Math.random() * tower.size());
			int temp = tower.get(rand);
			tower.set(rand, tower.get(i));
			tower.set(i, temp);
		}
		
	}
	
	public int[] newTower(int initHeight) {
		int[] newT = new int[initHeight];
		for(int i = 0; i < newT.length; i ++) {
			newT[i] = tower.remove(0);
		}
		return newT;
	}

	public void replaceA(Deck x){
		x.getTower().add(0, tower.remove(0));
	}
	
	
	public String showCard(){
		   String result = Integer.toString(tower.get(0));
		   return result;
	}
	
	public void replace(int index, int[] playerT, Deck x) {
		int temp = playerT[index];
		playerT[index] = tower.remove(0);
		x.getTower().add(0, temp);
	}

	public ArrayList<Integer> getTower(){
		return tower;
	}
	public String toString() {
		String sum = "";
		for(int i = 0; i < tower.size(); i ++ ) {
			sum += Integer.toString(tower.get(i)) + "\n";
		}
		return sum;
	}
}
