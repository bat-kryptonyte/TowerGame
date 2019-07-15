package tower_blaster;
import java.util.*;
public class Driver {
	public static void main(String[] args) {
		while(true){
			Scanner kb = new Scanner(System.in);
			System.out.println("Please enter your tower length");
			int tl = kb.nextInt();
			Deck tower = new Deck(tl - 1);
			Deck discardPile = new Deck(1);
			tower.shuffle();
			int[] pt = tower.newTower(10);
			int[] vikings = tower.newTower(10);
			while(! isWin(pt) && ! isWin(vikings)){
				System.out.println(tower.displayTower(pt));

				System.out.println("The card you can choose is: " + discardPile.showCard() + "or you can choose UNKNOWN");
				String userInput = kb.next();
				if(userInput.equalsIgnoreCase(discardPile.showCard())){
					System.out.println("Please enter the block you wish to switch");
					int userChoice = kb.nextInt();
					int ind = tower.getIndex(userChoice, pt); //weird method tb fixed
					discardPile.replace(ind, pt, discardPile);
				}else if(userInput.equalsIgnoreCase("UNKNOWN")){
					System.out.println("The card you can choose is: " + tower.showCard());
					System.out.println("Please choose YES, or DISCARD(YOUR TURN WILL BE SKIPPED");
					String uI = kb.next();
					if(uI.equalsIgnoreCase("YES")){
						System.out.println("Please enter the block you wish to switch");
						int userChoice = kb.nextInt();
						int ind = tower.getIndex(userChoice, pt);// weird method to be fixed
						tower.replace(ind, pt, discardPile);
					}else if(uI.equalsIgnoreCase("DISCARD")){
						tower.replaceA(discardPile);
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
