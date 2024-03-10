import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-space',
  templateUrl: './space.component.html',
  styleUrls: ['./space.component.css']
})
export class SpaceComponent{
/*   id = 0;
  productTitle!: string;
  productDescription!: string;
  productImage!: string;
  productState!: boolean;
  productId!: number;
  productDate!: Date;
  exist:boolean=true;
  isLoading:boolean=true;
 */
  id = 0;
  productTitle: string="titulo";
  productDescription: string="descripcion";
  productImage: string="Link Imagen";
  productState: boolean= true;
  productId: number= 5;
 // productDate: Date;
  exist:boolean=true;
  isLoading:boolean=false;
}
