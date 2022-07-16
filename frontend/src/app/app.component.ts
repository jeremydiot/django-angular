import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  opened!: boolean;
  title = 'project';

  onToggleSideBar() {
    this.opened = !this.opened;
  }

  ngOnInit(): void {
    this.opened = true;
  }

}
