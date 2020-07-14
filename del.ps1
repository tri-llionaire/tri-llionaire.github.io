string currentDirectory = Directory.GetCurrentDirectory();
string folderToDelete = String.Empty;
using(OpenFileDialog d = new OpenFileDialog())
{
	//Do something
	folderToDelete = Path.GetDirectoryName(d.FileName);
}
Directory.SetCurrentDirectory(currentDirectory);
Directory.Delete(folderToDelete);