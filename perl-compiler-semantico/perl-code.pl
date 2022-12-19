# Calculadora

$numero1 = 10.5;
$numero2 = $numero1 * 3;

$soma1 = 0;
$soma2 = 0;
$subtr1 = 0;
$subtr2 = 0;
$multi1 = 0;
$multi2 = 0;
$div1 = 1;
$div2 = 1;
$mod1 = 1;
$mod2 = 1;

print "Operação com $numero1 e $numero2";

sub soma($soma1, $soma2){
    $res = $soma1 + $soma2;
    return $res;
}

sub subtr($subtr1, $subtr2){
    $res2 = $subtr1 - $subtr2;
    return $res2;
}

sub multi($multi1, $multi2){
    $res3 = $multi1 * $multi2;
    return $res3;
}

sub div($div1, $div2){
    $res4 = $div1 / $div2;
    return $res4;
}

sub mod($mod1, $mod2){
    $res5 = $mod1 % $mod2;
    return $res5;
}

$soma = soma();
#$soma = soma($numero1, $numero2);
#$soma = soma($numero1, $numero2);
$subtr = subtr();
$multi = multi();
$div = div();
$mod = mod();
#$subtr = subtr($numero1, $numero2);
#$multi = multi($numero1, $numero2);
#$div = div($numero1, $numero2);
#$mod = mod($numero1, $numero2);

say "$soma, $subtr, $multi, $div, $mod";

@arrayOfNumbers = (-10, +10, -30.30 , 450.40);

$cont = 3;
while ( $cont > 0 ){
    print "$arrayOfNumbers[$cont]";
    $cont = $cont - 1;
}

@arrayOfStrings = ("Let's do it!", 'Is perl lexer ready?');

