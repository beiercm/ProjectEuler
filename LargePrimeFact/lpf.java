import java.util.*;
import java.math.*;

public class lpf
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		String numStr = input.next();
		BigInteger num = new BigInteger(numStr);
		BigInteger one = new BigInteger("1");
		BigInteger zero = new BigInteger("0");
		BigInteger div = new BigInteger("2");
		BigInteger bigMod;

		int i;

		while(num.compareTo(one) > 0)
		{
			bigMod = num.mod(div);

			if(bigMod.equals(zero))
				num = num.divide(div);
			else
				div = div.add(one);
		}

		System.out.println(div.toString());

	}
}