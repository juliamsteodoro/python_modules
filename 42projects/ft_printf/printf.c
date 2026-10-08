/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printf.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/11 11:24:39 by jumoreir          #+#    #+#             */
/*   Updated: 2026/06/17 18:56:04 by jumoreir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	parser(char const c, va_list list, int *count)
{
	if (c == 'c')
		ft_putchar(va_arg(list, int), count);
	else if (c == 's')
		ft_putstr(va_arg(list, char *), count);
	else if (c == 'd' || c == 'i')
		ft_putnbr(va_arg(list, int), count);
	else if (c == 'x' || c == 'X')
		ft_putnbr_hexa(va_arg(list, unsigned int), c, count);
	else if (c == 'u')
		ft_putnbr_unsigned(va_arg(list, unsigned int), count);
	else if (c == 'p')
		ft_putnbr_pointer(va_arg(list, void *), count);
	else if (c == '%')
		ft_putchar('%', count);
	return ;
}

int	ft_printf(const char *arg, ...)
{
	va_list	list;
	int		count;
	int		i;

	count = 0;
	i = 0;
	va_start(list, arg);
	while (arg[i] != '\0')
	{
		if (arg[i] == '%')
		{
			parser(arg[i + 1], list, &count);
			i = i + 2;
		}
		else
			ft_putchar(arg[i++], &count);
	}
	va_end (list);
	return (count);
}
