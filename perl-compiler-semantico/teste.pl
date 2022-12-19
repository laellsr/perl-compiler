# Calculadora

$numero1 = 10.5;
$numero2 = $numero1 * 3;

#$var = 3

$soma1 = 0;
$soma2 = 0;

$subtr1 = 0;
$subtr2 = 0;

#print ;

sub soma($soma1, $soma2){
    $res = $soma1 + $soma2;
    return $res;
}

sub subtr($subtr1, $subtr2){
    $res2 = $subtr1 - $subtr2;
    return $res2;
}

$fim = soma($numero1, $numero2);
$fim2 = soma($fim, $numero1);
$fim3 = subtr($fim, $fim2);
#teste