# Soma

$numero1 = 2;
#$numero1 = 'mu'
$numero2 = 1;
$soma1 = 0;
$soma2 = 0;

sub soma($soma1, $soma2){
    $res = $soma1 + $soma2;
    return $res;
}

#ERRO! Chamada de função com número errado de parâmetros.
$numero3 = soma($numero1, $numero2);