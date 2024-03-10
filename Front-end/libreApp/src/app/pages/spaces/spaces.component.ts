import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-spaces',
  templateUrl: './spaces.component.html',
  styleUrls: ['./spaces.component.css']
})
export class SpacesComponent {
  products:any[] = [
    {titulo:"titulo",
    id_publicacion:1
  },
  {titulo:"titulo2",
    id_publicacion:2
  },
  {titulo:"titulo3",
    id_publicacion:3
  }
  ];
  isEmpty:boolean = false;
isLoading:boolean = false;

constructor(private router: Router){}



publishById(id:number): void{
  this.router.navigate(['/', id]);
}
}
