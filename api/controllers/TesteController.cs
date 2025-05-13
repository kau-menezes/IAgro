using Microsoft.AspNetCore.Mvc;

namespace Server.Controllers;

[Route("/test")]
[ApiController]

public class TesteController() : ControllerBase {

    [HttpGet]
    public IActionResult Test(){
        return Ok("Server running");
    }
}