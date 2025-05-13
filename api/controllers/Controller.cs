using Microsoft.AspNetCore.Mvc;
using Server.Models;

namespace Server.Controllers;

[Route("/")]
[ApiController]

public class Controller() : ControllerBase {

    [HttpPost]
    public IActionResult Control([FromBody] Data data){
        if(data == null)
            return BadRequest("Data missing");

        foreach (var item in data.data){
            if(Dados.Data.ContainsKey(item.Key))
                continue;
            Dados.Data.Add(item.Key, item.Value);
        }

        if(data.sinal == 0) 
            return Ok("Tudo certo cabo antes");
        
        foreach (var item in Dados.Data){
            Console.WriteLine(item.Key);
            Console.WriteLine(item.Value);
        }

        Dados.Data.Clear();
        return Ok("Tudo certo");
    }
}