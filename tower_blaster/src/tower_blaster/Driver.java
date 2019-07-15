package tower_blaster;
import java.util.*;
public class Driver {
	public static final int USER_TOWER_HEIGHT = 10;
	public static void main(String[] args) {
		while(true){
			Scanner kb = new Scanner(System.in);
			System.out.println("Please enter your tower length");
			int tl = kb.nextInt();
			int score = 0;
			Deck tower = new Deck(tl);
			tower.shuffle();
			int[] pt = tower.newTower(USER_TOWER_HEIGHT);
			int[] vikings = tower.newTower(USER_TOWER_HEIGHT);
			Deck discardPile = new Deck(0);
			tower.replaceA(discardPile);
			System.out.println(displayTower(pt));
			while(! isWin(pt) || ! isWin(vikings)){
				//User steps

				System.out.println("The card you can choose is: " + discardPile.showCard() + " or you can choose UNKNOWN");
				System.out.println("Please select your choice: ");
				String userInput = kb.next();
				if(userInput.equalsIgnoreCase(discardPile.showCard())){
					System.out.println("Please enter the block you wish to switch: ");
					int userChoice = kb.nextInt();
					int ind = getIndex(userChoice, pt); 
					discardPile.replace(ind, pt, discardPile);
					score += getScore(pt, ind);
					System.out.println(displayTower(pt));
					System.out.println("Your score is currently at : " + score);
				}else if(userInput.equalsIgnoreCase("UNKNOWN")){
					System.out.println("The card you can choose is: " + tower.showCard());
					System.out.println("Please choose YES, or DISCARD(YOUR TURN WILL BE SKIPPED: ");
					String uI = kb.next();
					if(uI.equalsIgnoreCase("YES")){
						System.out.println("Please enter the block you wish to switch: ");
						int userChoice = kb.nextInt();
						int ind = getIndex(userChoice, pt);
						tower.replace(ind, pt, discardPile);
						score += getScore(pt, ind);
						System.out.println(displayTower(pt));
						System.out.println("Your score is currently at : " + score);
					}else if(uI.equalsIgnoreCase("DISCARD")){
						tower.replaceA(discardPile);
						System.out.println(displayTower(pt));
					}
				}

				//Viking steps
				boolean step1 = Math.random() < 0.5;
				boolean step2 = Math.random() < 0.5;
				int randV = (int)(Math.random() * USER_TOWER_HEIGHT);
				int randV2 = (int)(Math.random() * USER_TOWER_HEIGHT);
				if(step1){
					discardPile.replace(randV, vikings, discardPile);
				}else{
					if(step2){
						tower.replace(randV2, vikings, discardPile);
					}else{
						tower.replaceA(discardPile);
					}
				}
				if(isWin(pt)) {
					break;
				}else if(isWin(vikings)){
					break;
				}

			}
            if (isWin(pt)) {
				System.out.println("Congratulations! You have won!");
				System.out.println("Would you like to play again(YES or NO): ");
				String input = kb.next();
				if(input.equalsIgnoreCase("YES")){
					continue;
				}else{
					kb.close();
					break;
				}
			} else if (isWin(vikings)) {
				System.out.println("You have lost! Good Luck next time!");
				System.out.println("Would you like to play again(YES or NO): ");
				String input = kb.next();
				if (input.equalsIgnoreCase("YES")) {
					continue;
				} else {
					kb.close();
					break;
				}
			}
   

		}
		
	}
	
	public static int getScore(int[] playerTower, int userIndex){
		ArrayList<Integer> tempPile = new ArrayList<Integer>();
		int count = 0;
		int arrInd = 0;
		for(int i = 1; i < playerTower.length; i ++){
			if(playerTower[i] - playerTower[i - 1] == 1){
				tempPile.add(i - 1);
				if(i - 1 == userIndex){
					arrInd = tempPile.get(tempPile.size() - 1);
				}
			}
		}
		for(int i = 0; i < tempPile.size(); i ++){
			if(tempPile.get(arrInd) - tempPile.get(i) == arrInd - i){
				count ++;
			}
		}
		return (int) (Math.pow(count, 2) * playerTower[userIndex]);
	}
	
	public static int getIndex(int block, int[] us){
		int index = 0;
		for (int i = 0; i < us.length; i++) {
			if (us[i] == block) {
				index = i;
			}
		}
		return index;
	}

	public static String displayTower(int[] pt) {
		String result = "";
		for (int i = 0; i < pt.length; i++) {
			result += pt[i] + " ";
		}
		return "This is your deck: " + result;

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
