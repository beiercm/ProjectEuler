import java.math.*;

public class LargestPrimeFactor
{
	public static void main(String[] args)
	{
		System.out.println(findLargestPrimeFactor(new BigInteger("600851475143")));
	}

	public static int findLargestPrimeFactor(BigInteger n)
	{
		BigInteger div = new BigInteger("2");
		BigInteger zero = new BigInteger("0");
		
		while(n.mod(div).equals("0"))
			n = n.divide(div);

		div = new BigInteger("3");

		while(!n.equals(div))
		{
			if(n.mod(div).equals(zero))
				n = n.divide(div);
			else
				div = div.add(new BigInteger("2"));
		}	

		return Integer.parseInt(div.toString());
	}
}