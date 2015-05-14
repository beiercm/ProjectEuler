public class Multiples
{
	public static void main(String[] args)
	{
		System.out.println(multiples(1000, 3, 5));
	}

	public static int multiples(int n, int a, int b)
	{
		int sum = 0;

		for(int i = 0; i < n; i++)
			if(i % a == 0 || i % b == 0)
				sum += i;

		return sum;
	}
}