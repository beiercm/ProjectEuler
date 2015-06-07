public class Prime10001st
{

	static int[] primeArray;

	public static void main(String[] args)
	{
		int primeCount = 10001;

		primeArray = seedPrimeArray(primeCount);
		primeArray = findPrimes(primeArray);
		//printArray(primeArray);
		System.out.println(primeArray[primeCount - 1]);
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

	public static void printArray(int[] array)
	{
		for(int i = 0; i < array.length; i++)
			System.out.println(array[i]);
	}
}