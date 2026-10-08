
/*
./push_swap "3 1 2"

argc == 1? não → continua
argc == 2? sim → ft_split → ["3", "1", "2", NULL]

count_size(["3","1","2",NULL]):
  percorre até NULL → retorna 3

percorre cada string com ft_isvalidnbr:
  "3" → ok
  "1" → ok
  "2" → ok

converte cada string com ft_atol + checa INT_MAX/INT_MIN:
  "3" → 3 → ok
  "1" → 1 → ok
  "2" → 2 → ok
  resultado: nums = [3, 1, 2]

ft_isduplicate(nums, size=3):
  i=0, j=1 → 3 == 1? não
  i=0, j=2 → 3 == 2? não
  i=1, j=2 → 1 == 2? não
  → sem duplicatas!

tudo válido → cria a pilha [3, 1, 2]
*/