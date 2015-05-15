public class EvenFib
{
	public static void main(String[] args)
	{
		System.out.println(findEvenFibSum(100));
	}

	 public static int findEvenFibSum(int upperLimit)
	 {
	 	int sum = 0, f1 = 1, f2 = 1, f3 = 0;

	 	while(f3 < upperLimit)
	 	{
	 		f3 = f2 + f1;

	 		if(f3 % 2 == 0)
	 			sum += f3;

	 		f1 = f2;
	 		f3 = f2;
	 	}

	 	return sum;
	 }
}