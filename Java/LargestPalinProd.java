public class LargestPalinProd
{
	public static void main(String[] args)
	{
		System.out.println(findLargestPalinProd());
		System.out.println(findLargestPalinProdBetter());
	}

	//Brute force method
	public static int findLargestPalinProd()
	{
		int maxPalindrome = 0, num;

		for(int i = 100; i < 999; i++)
		{
			for(int j = i; j < 999; j++)
			{
				num = i * j;

				if(isPalindrome(num))
				{
					if(num > maxPalindrome)
						maxPalindrome = num;
				}
			}
		}

		return maxPalindrome;
	}

	//Different approach
	public static int findLargestPalinProdBetter()
	{
		int palin = 0;
		int firstHalf = 998;
		Boolean found = false;

		while(!found)
		{
			firstHalf--;

			palin = makePalindrome(firstHalf);

			for(int i = 999; i >= 100; i--)
			{
				if((palin / i) > 999 || i*i < palin)
					break;

				if((palin % i == 0))
				{
					found = true;
					break;
				}
			}
		}

		return palin;
	}

	//Only works for three digit numbers since that's what the problem
	//is asking for
	public static int makePalindrome(int firstHalf)
	{	
		int palin = firstHalf * 1000;
		int secondHalf = 0;

		while(firstHalf > 1)
		{	
			secondHalf = (secondHalf * 10) + (firstHalf % 10);
			firstHalf /= 10;
		}

		palin += secondHalf;
		
		return palin;
	}

	public static Boolean isPalindrome(int num)
	{
		String n = Integer.toString(num);

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
