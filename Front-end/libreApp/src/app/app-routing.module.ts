import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SpaceComponent } from './pages/space/space.component';
import { SpacesComponent } from './pages/spaces/spaces.component';

const routes: Routes = [
  {path: '', component:SpacesComponent},
  {path: ':id', component:SpaceComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
