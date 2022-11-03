# Calculadora

$numero1 = 10.5;
$numero2 = $numero1 * 3

print "Operação com $numero1 e $numero2";

sub soma($numero1, $numero2){
    $res = $numero1 + $numero2;
    return $res;
}

sub subtr($numero1, $numero2){
    $res = $numero1 - $numero2;
    return $res;
}

sub multi($numero1, $numero2){
    $res = $numero1 * $numero2;
    return $res;
}

sub div($numero1, $numero2){
    $res = $numero1 / $numero2;
    $erro = 'não podemos dividir por zero';
    if ( $numero2 == 0 ){
        return $erro;
    }
    return $res;
}

sub mod($numero1, $numero2){
    $res = $numero1 % $numero2;
    return $res;
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