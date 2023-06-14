unit uMain;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation, FMX.TabControl, FMX.Layouts, FMX.Objects;

type
  TFormMain = class(TForm)
    ToolBarTop: TToolBar;
    LblTitle: TLabel;
    TabControl1: TTabControl;
    TabItemAPOD: TTabItem;
    TabItemAsteroids: TTabItem;
    TabItemInsights: TTabItem;
    Label1: TLabel;
    LayoutTitle: TLayout;
    BtnFetchAPOD: TButton;
    LayoutDetails: TLayout;
    LayoutInformation: TLayout;
    LayoutImage: TLayout;
    Image1: TImage;
    LblAPODDate: TLabel;
    LblAPODTitle: TLabel;
    LblAPODExplanation: TLabel;
    StyleBook1: TStyleBook;
    procedure BtnFetchAPODClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FormMain: TFormMain;

implementation

{$R *.fmx}

procedure TFormMain.BtnFetchAPODClick(Sender: TObject);
begin
  // pass
end;

end.
