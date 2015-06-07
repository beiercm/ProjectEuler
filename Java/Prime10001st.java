public class Prime10001st
{
	public static void main(String[] args)
	{
		System.out.println(findNthPrime(10001));
	}

	public static int findNthPrime(int n)
	{
		int[] primeArray = seedPrimeArray(n);
		primeArray = findPrimes(primeArray);

		return primeArray[n - 1];
	}

	public static int[] seedPrimeArray(int n)
	{
		int[] primeArray = new int[n];
		primeArray[0] = 2;

		return primeArray;
	}

	public static int[] findPrimes(int[] primeArray)
	{
		int index = 1;
		int num = 3;
		
		for(int i = 0; index < primeArray.length; i++)
		{
			if((primeArray[i] * primeArray[i]) > num || i == index)
			{
				primeArray[index] = num;
				num += 2;
				index++;
				i = 0;
			}

			if(num % primeArray[i] == 0)
			{
				num += 2;
				i = 0;
			}
		}

		return primeArray;	
	}	
}