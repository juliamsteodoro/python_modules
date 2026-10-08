/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 11:59:41 by jumoreir          #+#    #+#             */
/*   Updated: 2026/06/19 14:24:30 by jumoreir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putchar(char c, int *count)
{
	*count += write(1, &c, 1);
}

void	ft_putstr(char *s, int *count)
{
	size_t	i;

	i = 0;
	if (!s)
		s = "(null)";
	while (s[i])
	{
		ft_putchar(s[i], count);
		i++;
	}
}

void	ft_putnbr(int n, int *count)
{
	long	nb;
	char	nbr;

	nb = n;
	if (nb < 0)
	{
		ft_putchar('-', count);
		nb = -nb;
	}
	if (nb > 9)
		ft_putnbr(nb / 10, count);
	nbr = (nb % 10) + '0';
	*count += write(1, &nbr, 1);
}

void	ft_putnbr_hexa(unsigned int n, char format, int *count)
{
	char	*base;
	char	buffer[sizeof(char) * 2];
	int		i;

	i = 0;
	if (n == 0)
	{
		*count += write(1, "0", 1);
		return ;
	}
	if (format == 'X')
		base = "0123456789ABCDEF";
	else
		base = "0123456789abcdef";
	while (n > 0)
	{
		buffer[i++] = base[n % 16];
		n = n / 16;
	}
	while (--i >= 0)
		*count += write(1, &buffer[i], 1);
	return ;
}

void	ft_putnbr_unsigned(unsigned int n, int *count)
{
	char	nbr;

	if (n > 9)
		ft_putnbr_unsigned(n / 10, count);
	nbr = (n % 10) + '0';
	*count += write(1, &nbr, 1);
}
