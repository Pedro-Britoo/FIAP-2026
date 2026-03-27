// Métodos básicos
console.log("Mensagem normal");
console.info("Informação");
console.warn("Aviso");
console.error("Erro");

// Tabelas
console.table([
  { id: 1, tarefa: "Estudar JS" },
  { id: 2, tarefa: "Praticar código" }
]);

// Agrupamento
console.group("Grupo de logs");
console.log("Log 1");
console.log("Log 2");
console.groupEnd();

// Medição de tempo
console.time("Timer");
// ...algum processamento...
console.timeEnd("Timer");

//----------------------------------------------

// Com var (escopo de função)
var antigo = "Forma antiga de declarar variáveis";

// Com let (escopo de bloco, pode ser reatribuída)
let userName = "Maria";
userName = "João"; // permitido

// Com const (escopo de bloco, não pode ser reatribuída)
const API_URL = "https://api.example.com";
// API_URL = "..."; // Erro
