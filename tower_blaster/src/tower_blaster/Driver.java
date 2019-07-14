package tower_blaster;
import java.util.Scanner;
public class Driver {
	public static void main(String[] args) {
		while(true){
			Scanner kb = new Scanner(System.in);
			Deck tower = new Deck(50);
			tower.shuffle();
			int[] pt = tower.newTower(10);
			int[] vikings = tower.newTower(10);
			while(! isWin(pt) && ! isWin(vikings)){
				System.out.println(tower.displayTower(pt));

				System.out.println("The card you can choose is: " + tower.showCard() + "or you can choose UNKNOWN");
				String userInput = kb.next();
				if(userInput.equalsIgnoreCase(tower.showCard())){
					System.out.println("Please enter the block you wish to switch");
					int userChoice = kb.nextInt();
					int ind = tower.getIndex(userChoice);
					tower.replace(ind, pt);
				}else if(userInput.equalsIgnoreCase("UNKNOWN")){
					System.out.println("Please choose YES, or DISCARD(YOUR TURN WILL BE SKIPPED");
					String uI = kb.next();
					if(uI.equalsIgnoreCase("YES")){
						System.out.println("The card you can choose is: " + tower.showCard());
					}
				}
			}



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
