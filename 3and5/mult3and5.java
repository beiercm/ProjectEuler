public class mult3and5
{
	public static void main(String[] args)
	{
		int n = 0, sum = 0;

		while(n < 1000)
		{
			if(n % 3 == 0 || n % 5 == 0)
				sum += n;
			n++;
		}

		System.out.printf("%d\n", sum);
	}
}