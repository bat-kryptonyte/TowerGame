package tower_blaster;
import java.util.*;

public class Deck {
	private  ArrayList<Integer> tower;
	
	public Deck(int initSize)
	{
		tower = new ArrayList<Integer>();
		for(int i = 0; i <= initSize; i ++) {
			tower.add(i + 1);
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
	
	public int getIndex(int block, int[] us){
		int index = 0;
		for(int i = 0; i < us.length; i ++){
			if(us[i] == block){
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
    /*
	public ArrayList<Integer> discardPile(){
		ArrayList<Integer> newP = new ArrayList<Integer>();
		newP.add(tower.remove(0));
		return newP;
	}
	*/

	public void replaceA(Deck x){
		x.getTower().add(tower.remove(0), 0);
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

	public String displayTower(int[] pt){
		String result = "";
		for(int i = 0; i < pt.length; i ++){
            result += pt[i] + " ";
		}
		return "This is your deck: " + result;

	}
//Test
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
