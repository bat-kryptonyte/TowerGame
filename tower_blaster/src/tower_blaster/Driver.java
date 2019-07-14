package tower_blaster;
import java.util.Scanner;
public class Driver {
	public static void main(String[] args) {
		while(true){
			Deck tower = new Deck(50);
			tower.shuffle();
			int[] pt = tower.newTower(10);
			int[] vikings = tower.newTower(10);
			



		}
		
	}
	
	public static boolean isWin(int[] playerTower) {
		boolean value = true;
		int[] pt = new int[playerTower.length];
		for(int i = 0; i < pt.length; i ++) {
			pt[i] = playerTower[i];
		}
		for(int i = 1; i < pt.length; i ++) {
			if(pt[i] < pt[i - 1]) {
				int temp = pt[i];
				pt[i] = pt[i - 1];
				pt[i - 1] = temp;
			}
		}
		for(int i = 0; i < playerTower.length; i ++) {
			if(pt[i] != playerTower[i]) {
				return false;
			}
		}
		return value;
	}
}
