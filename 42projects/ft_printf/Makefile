# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/17 18:18:09 by jumoreir          #+#    #+#              #
#    Updated: 2026/06/17 18:25:30 by jumoreir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	=	libftprintf.a

CC		=	cc
CFLAGS	= 	-Wall -Wextra -Werror
AR		=	ar rcs

SRCS 	=	ft_printf_utils.c \
			ft_putnbr_pointer.c \
			printf.c \

OBJS	=	$(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re:	fclean all

bonus:	all

.PHONY: all clean fclean re bonus