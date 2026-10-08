/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_pointer.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/17 11:19:23 by marvin            #+#    #+#             */
/*   Updated: 2026/06/17 11:19:23 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putnbr_pointer(void *ptr, int *count)
{
	unsigned long	pointer ;
	char			buffer[sizeof(unsigned long) * 2];
	int				i;
	char			*base;

	i = 0;
	base = "0123456789abcdef";
	pointer = (unsigned long)ptr;
	if (!ptr)
	{
		ft_putstr("(nil)", count);
		return ;
	}
	ft_putstr("0x", count);
	while (pointer)
	{
		buffer[i++] = base[pointer % 16];
		pointer = pointer / 16;
	}
	while (--i >= 0)
		*count += write(1, &buffer[i], 1);
	return ;
}
