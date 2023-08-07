import java.util.*;

public class Capitalize {
	public static void main (String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("What do you want to capitalize?");
		String s = scanner.nextLine();
		System.out.println(s.toUpperCase());
	}
}
