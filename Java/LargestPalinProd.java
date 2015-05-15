public class LargestPalinProd
{
	public static void main(String[] args)
	{
		System.out.println(isPalindrome2(Integer.toString(101)));
	}

	public static Boolean isPalindrome(String n)
	{
		int i = 0, j = n.length() - 1;

		while(j > i)
			if(n.charAt(i++) != n.charAt(j--))
				return false;

		return true;
	}

	public static Boolean isPalindrome2(String n)
	{
		return palinCheckRecur(n, 0, n.length() - 1);
	}

	public static Boolean palinCheckRecur(String n, int i, int j)
	{
		if(j < i)
			return true;

		return (n.charAt(i) == n.charAt(j)) && palinCheckRecur(n, i + 1, i - 1);
	}
}