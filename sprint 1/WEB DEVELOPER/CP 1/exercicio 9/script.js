//Repositório para o Checkpoint #1 de Engenharia de Software
//Questão 1

//node -v;
//v24.14.0

//npm -v;
//11.9.0

//git --version;
//git version 2.53.0.windows.2

//Questão 2

console.log('Mensagem inicial');
alert('Bem-vindo ao Checkpoint!');

//Questão 3

//Repositório e Primeiro Commit

//Questão 4

var valor1 = 1;
var valor2 = 4;

let valor3 = 6;
let valor4 = 9;

const valor5 = 12;
const valor6 = 16;

console.log(valor1);
console.log(valor2);
console.log(valor3);
console.log(valor4);
console.log(valor5);
console.log(valor6);

//Questão 5

let aa = 10;
let bb = 5;

console.log(aa + bb);
console.log(aa - bb);
console.log(aa * bb);
console.log(aa / bb);

//Questão 6

let primeiro_numero = '8';
let segundo_numero = 8;

console.log(primeiro_numero == segundo_numero);
console.log(primeiro_numero === segundo_numero);

let terceiro_numero = '4';
let quarto_numero = 4;

console.log(terceiro_numero != quarto_numero);
console.log(terceiro_numero !== quarto_numero);

let quinto_numero = 6;
let sexto_numero = 9;

console.log(quinto_numero < sexto_numero);

//Questão 7

temIdade = true;
temTitulo = false;
saldo = 100;

console.log("Pode votar? (Idade E Título):", temIdade && temTitulo); 

console.log("Pode entrar na festa? (Idade OU Título):", temIdade || temTitulo);

console.log("Não tem título?", !temTitulo);

console.log("Saldo é positivo?", saldo > 0 && temIdade);

//Questão 8
//Exemplo de branch e merge 



//exercicio 9

function compararNumeros(a, b) {
  if (a > b) {
    return "A é maior";
  } else if (b > a) {
    return "B é maior";
  } else {
    return "Os dois são iguais";
  }
}

console.log(compararNumeros(5, 10)); 
console.log(compararNumeros(10, 5));
console.log(compararNumeros(7, 7));

// exercicio 10

let a = 5;
let b = 3;
console.log("soma:", a + b);

let x = true;
let y = false;

console.log(x && y);
console.log(x || y);
