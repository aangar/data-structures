import java.util.Optional;
import binarytrees.BinaryTreeTest;

public class Main {
	public static void main(String[] args) {
		Optional<String> module = Optional.ofNullable(args[0]);
		if (!module.isEmpty()) {
			String mod = module.get();
			System.out.println(mod);
			if (mod.equals("binarytree")) {
				BinaryTreeTest.runTestCases();
			}
		}
	}
}