#![allow(unused)]
use chrono::Utc;
use sha2::{Digest, Sha256};
use std::collections::LinkedList;
use std::path::PathBuf;

// ----------------------------
// TODO: Implement a way to get the head on command
// TODO: Implement a way to serialize the linkedlist and save it to a file and load it from a file and deserialize it
// TODO: Implement a way to save the revisions to the .mach folder (save all files from tracking list - make sure folder are created too)
// ----------------------------

/// A revision is a snapshot of all the files in the repository at a particular time.
struct Revision {
    /// # Arguments
    /// * `id` - id of the revision (defualt: hash of the content of the files)
    /// * `user` - user who created the revision (default: 'Anonymous')
    /// * `date` - date when the revision was created (default: current time if not set)
    /// * `folder_name` - name of the folder where the revision is stored
    /// * `files` - list of files in the revision (from the tracking list)
    ///
    id: String,
    user: String,
    date: String,
    folder_path: String,
    files: Vec<String>,
}

impl Revision {
    /// Create a plain new revision
    pub fn new() -> Self {
        Self {
            id: String::from("0"),
            user: String::from("Anonymous"),
            date: Utc::now().timestamp().to_string(),
            folder_path: String::from(""),
            files: vec![],
        }
    }

    /// Set the user who created the revision
    pub fn set_user(&mut self, user: String) {
        self.user = user;
    }

    /// Set the id of the revision
    pub fn set_id(&mut self, id: String) {
        self.id = id;
    }

    /// Set the date of the revision
    pub fn set_date(&mut self, date: String) {
        self.date = date;
    }

    /// Set the folder name of the revision
    pub fn set_folder_name(&mut self, folder_name: String) {
        self.folder_path = folder_name;
    }

    /// Sets the files of the revision from the tracking list
    pub fn set_files(&mut self, files: Vec<String>) {
        self.files = files;
    }
}

/// A tracking list is a list of files that are tracked by the repository.
struct TrackingList {
    /// # Arguments
    /// * `files` - list of files paths
    files: Vec<String>,
}

impl TrackingList {
    /// Create a new tracking list
    pub fn new() -> Self {
        Self { files: vec![] }
    }

    /// Add a file to the tracking list
    pub fn add_file(&mut self, path: String) {
        self.files.push(path);
    }

    /// Remove a file from the tracking list
    pub fn remove_file(&mut self, path: &str) {
        self.files.retain(|p| p != path);
    }

    /// Get the list of files in the tracking list
    pub fn return_list(&self) -> &Vec<String> {
        &self.files
    }
}

/// A repository is a collection of revisions.
struct Repository {
    /// # Arguments
    /// * `path` - path to the repository (same level as .mach folder)
    /// * `tracking_list` - list of files that are tracked by the repository
    /// * `revisions` - list of revisions in the repository represented as a singly linked list
    path: String,
    tracking_list: TrackingList,
    revisions: LinkedList<Revision>,
}

impl Repository {
    /// Create a new repository
    fn new(path: &str) -> Self {
        Self {
            path: String::from(path),
            tracking_list: TrackingList::new(),
            revisions: LinkedList::new(),
        }
    }

    /// Add a revision to the repository
    fn add_revision(&mut self, revision: Revision) {
        self.revisions.push_back(revision);
    }

    /// Remove a revision from the repository
    fn remove_revision(&mut self) {
        self.revisions.pop_back();
    }

    /// Get the last revision in the repository
    fn add_to_tracking_list(&mut self, path: String) {
        self.tracking_list.add_file(path);
    }

    /// Remove a file from the tracking list
    fn remove_from_tracking_list(&mut self, path: &str) {
        self.tracking_list.remove_file(path);
    }

    /// Get the list of files in the tracking list
    fn return_tracking_list(&self) -> &Vec<String> {
        self.tracking_list.return_list()
    }

    /// Find the difference between two revisions
    // fn find_difference(&self, revision1: &Revision, revision2: &Revision) -> Vec<String> {
    //     // let mut difference = vec![];
    //     // difference

    //     // TODO: Implement finding the difference between two revisions
    //     vec![revision1., revision2]
    // }

    /// Print the history log of the repository
    fn log(&self) {
        // TODO: Implement history log of the repository
        // Start by going through the revisions and comparing one to the next (pairs of 2) in linkedlist
        // and calling the diff function
        // then return out a list of the differences and each revision data (id, user, date) for printing
    }
}

pub fn return_hash(path: &str) -> String {
    // TAKE I/O FROM EZRA'S MODULE AND DELETE BOTTOM

    let mut file = std::fs::File::open(path).unwrap();
    let mut file_content = String::new();

    std::io::Read::read_to_string(&mut file, &mut file_content).unwrap();

    let mut hasher = Sha256::new();
    hasher.update(file_content);

    let result = hasher.finalize();

    let mut hash = String::new();

    for byte in result {
        hash.push_str(&format!("{:02x}", byte));
    }

    hash
}

fn main() {
    let mut repo = Repository::new("C:\\Users\\Desktop\\test");
    repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
    repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

    let mut rev = Revision::new();
    rev.set_user(String::from("user"));
    rev.set_files(repo.return_tracking_list().clone());
    repo.add_revision(rev);

    let mut rev2 = Revision::new();
    rev2.set_user(String::from("user2"));
    rev2.set_files(repo.return_tracking_list().clone());
    repo.add_revision(rev2);

    repo.return_tracking_list()
        .iter()
        .for_each(|f| println!("{}", f));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_revision() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        let mut rev = Revision::new();
        rev.set_user(String::from("user"));
        rev.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev);

        let mut rev2 = Revision::new();
        rev2.set_user(String::from("user2"));
        rev2.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev2);

        assert_eq!(repo.revisions.len(), 2);
    }

    #[test]
    fn test_remove_revision() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        let mut rev = Revision::new();
        rev.set_user(String::from("user"));
        rev.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev);

        let mut rev2 = Revision::new();
        rev2.set_user(String::from("user2"));
        rev2.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev2);

        repo.remove_revision();

        assert_eq!(repo.revisions.len(), 1);
    }

    #[test]
    fn test_add_to_tracking_list() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        assert_eq!(repo.tracking_list.files.len(), 2);
    }

    #[test]
    fn test_remove_from_tracking_list() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        repo.remove_from_tracking_list("C:\\Users\\user\\Desktop\\test\\test.txt");

        assert_eq!(repo.tracking_list.files.len(), 1);
    }

    #[test]
    fn test_return_tracking_list() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        assert_eq!(repo.return_tracking_list().len(), 2);
    }

    #[test]
    fn test_return_hash() {
        let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
        d.push(".gitignore");

        let path = d.to_str().unwrap();
        let hash = return_hash(path);

        assert_eq!(
            hash,
            "44c92e3a70ad3307b7056871c2bdb096d8bfa9373f5bf06a79bb6324a20ff2fb"
        );
    }

    #[test]
    fn test_diff() {
        let mut repo = Repository::new("C:\\Users\\Desktop\\test");
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test.txt"));
        repo.add_to_tracking_list(String::from("C:\\Users\\user\\Desktop\\test\\test2.txt"));

        let mut rev = Revision::new();
        rev.set_user(String::from("user"));
        rev.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev);

        let mut rev2 = Revision::new();
        rev2.set_user(String::from("user2"));
        rev2.set_files(repo.return_tracking_list().clone());
        repo.add_revision(rev2);

        // let diff = repo.diff(0, 1);
        //assert_eq!(diff.len(), 2);

        // uncomment above when diff is implemented ^^^
        assert_eq!(1, 1)
    }
}
