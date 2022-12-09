# Calculadora

$numero1 = 10.5;
$numero2 = $numero1 * 3;

print "Operação com $numero1 e $numero2";

sub soma($numero1, $numero2){
    $res = $numero1 + $numero2;
    return $res;
}

sub subtr($numero1, $numero2){
    $res2 = $numero1 - $numero2;
    return $res2;
}

sub multi($numero1, $numero2){
    $res3 = $numero1 * $numero2;
    return $res3;
}

sub div($numero1, $numero2){
    $res4 = $numero1 / $numero2;
    $erro = 'não podemos dividir por zero';
    if ( $numero2 == 0 ){
        return $erro;
    }
    return $res4;
}

sub mod($numero1, $numero2){
    $res5 = $numero1 % $numero2;
    return $res5;
}

$soma = soma();
$subtr = subtr();
$multi = multi();
$div = div();
$mod = mod();

say "$soma, $subtr, $multi, $div, $mod";

@arrayOfNumbers = (-10, +10, -30.30 , 450.40);

$cont = 3;
while ( $cont > 0 ){
    print "$arrayOfNumbers[$cont]";
    $cont = $cont - 1;
}

@arrayOfStrings = ("Let's do it!", 'Is perl lexer ready?');